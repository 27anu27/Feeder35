package com.bhatore.android.feeder35;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class loginpage extends AppCompatActivity implements Callback<GsonModels.UserDetails> {
    public Button loginbutton;
    Activity context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loginpage);



        SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
        //Toast.makeText(this,sharedPreference.getValue(),Toast.LENGTH_SHORT).show();

        if(sharedPreference.getLoggedin().equals("hi"))
        {
            gotomain();
        }


        loginbutton = (Button) findViewById(R.id.loginbutton);
        loginbutton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                EditText theFact =(EditText) findViewById(R.id.username);
                String text = theFact.getText().toString();
                EditText a = (EditText) findViewById(R.id.password);
                String pass = a.getText().toString();

                // Hides the soft keyboard
                InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
                imm.hideSoftInputFromWindow(findViewById(R.id.username).getWindowToken(), 0);
                imm.hideSoftInputFromWindow(findViewById(R.id.password).getWindowToken(), 0);
                TextView textView = (TextView) findViewById(R.id.aa);
                //textView.setText("Hello " + text);
                // Save the text in SharedPreference
                if (!text.isEmpty()&&!pass.isEmpty()) {
                    //SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
                    //sharedPreference.save(text, pass);
                    //HTTP request
                    //sharedPreference.loggedin="0";
                    RetrofitInterface retrofitInterface = ServiceGenerator.createService(RetrofitInterface.class);
                    retrofitInterface.getUserDetails(text,pass).enqueue(loginpage.this);
                } else {
                    restartActivity(context);
                }
            }
        });


    }

    public static void restartActivity(Activity act){

        Intent intent=new Intent();
        intent.setClass(act, act.getClass());
        act.startActivity(intent);
        act.finish();

    }
    public void gotomain()
    {
        Intent intent = new Intent(context , studentmain.class);
        EditText editText = (EditText) findViewById(R.id.username);
        String message = editText.getText().toString();
        intent.putExtra( "msg", message);
        startActivity(intent);
    }

    @Override
    public void onResponse(Call<GsonModels.UserDetails> call, Response<GsonModels.UserDetails> response) {
        if(response.isSuccessful()) {
            GsonModels.UserDetails userDetails = response.body();
            if(userDetails.getloggedin() == true) {
                SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
                sharedPreference.save(userDetails.getName(),userDetails.getEmail(),userDetails.getRollno());
                Toast.makeText(this,"Logged in",Toast.LENGTH_SHORT).show();
                gotomain();
                EditText theFact =(EditText) findViewById(R.id.username);
                theFact.setText("");
                EditText a = (EditText) findViewById(R.id.password);
                a.setText("");
            }
            else
                Toast.makeText(this,"Wrong Credentials",Toast.LENGTH_SHORT).show();
        }
        else {
            Toast.makeText(this,"Response Code: "+String.valueOf(response.code()),Toast.LENGTH_SHORT).show();
            restartActivity(this);
        }
    }


    @Override
    public void onBackPressed()
    {
        Intent i=new Intent(loginpage.this, MainActivity.class);
        startActivity(i);
    }

    @Override
    public void onFailure(Call<GsonModels.UserDetails> call, Throwable t) {
        Toast.makeText(this,"Wrong Credential or failed : ",Toast.LENGTH_SHORT).show();
    }
}
