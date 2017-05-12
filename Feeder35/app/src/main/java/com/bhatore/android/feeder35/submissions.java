package com.bhatore.android.feeder35;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

import static com.bhatore.android.feeder35.SharedPreference.roll;

public class submissions extends AppCompatActivity implements Callback<GsonModels.result>{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_submissions);
        Intent intent = getIntent();
        String quesids = intent.getStringExtra("qids");
        String roll = intent.getStringExtra("rollno");
        String t = intent.getStringExtra("ans");
        //Toast.makeText(this,"Successful!",Toast.LENGTH_SHORT).show();
        RetrofitInterface retrofitInterface = ServiceGenerator.createService(RetrofitInterface.class);
        retrofitInterface.sendanswers(quesids,roll,t).enqueue(submissions.this);
    }

    @Override
    public void onResponse(Call<GsonModels.result> call, Response<GsonModels.result> response) {
        TextView a = (TextView) findViewById(R.id.result);
        a.setText("Your Submissions are Successful\n\n Press back button to return to dashboard!");


    }

    @Override
    public void onBackPressed()
    {
        Intent i=new Intent(submissions.this, studentmain.class);
        startActivity(i);
    }




    @Override
    public void onFailure(Call<GsonModels.result> call, Throwable t) {
        TextView a = (TextView) findViewById(R.id.result);
        a.setText("Something went wrong :/");
    }
}
