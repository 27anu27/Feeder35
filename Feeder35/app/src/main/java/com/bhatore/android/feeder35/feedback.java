package com.bhatore.android.feeder35;

import android.app.Activity;
import android.content.Intent;
import android.media.Rating;
import android.support.design.widget.NavigationView;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.RatingBar;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class feedback extends AppCompatActivity implements Callback<GsonModels.aa>{
    String date;
    String roll;
    String meage;
    Activity con =this;
    String quesids="";
    int z=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_feedback);
        Intent intent = getIntent();
        String message = intent.getStringExtra("type");
        date = intent.getStringExtra("date");
        String course = intent.getStringExtra("course");
        meage = intent.getStringExtra("id");
        String feedback = intent.getStringExtra("feedback");
        roll = intent.getStringExtra("stud");
        //SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
        //roll = sharedPreference.getRoll();
//        Toast.makeText(getApplicationContext(),String.valueOf(roll),
//                Toast.LENGTH_SHORT).show();
//        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
//        View header=navigationView.getHeaderView(0);
//        TextView name =(TextView)header.findViewById(R.id.studentname);
//        roll = name.getText().toString();


        TextView a = (TextView) findViewById(R.id.toolbar_title);
        TextView b = (TextView) findViewById(R.id.courseheading);
        b.setText(course);
        TextView c = (TextView) findViewById(R.id.type);
        c.setText(message);
        TextView d = (TextView) findViewById(R.id.duedate);
        d.setText("Due Date : "+date);
        LinearLayout buttonContainer = (LinearLayout) findViewById(R.id.activity_feedback);
        if(feedback.equals("1")) {
            a.setText("FEEDBACK");


            Button button = new Button(this);
            buttonContainer.addView(button);
            button.setId(R.id.sub);
            button.setText("START");
            button.setHeight(12);
            button.setWidth(25);
            button.setOnClickListener(btn);

        }
        else
            a.setText("DEADLINE");

    }
    View.OnClickListener btn = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            RatingBar r = (RatingBar) findViewById(R.id.b1);


            RetrofitInterface retrofitInterface = ServiceGenerator.createService(RetrofitInterface.class);
            retrofitInterface.send(meage,roll).enqueue(feedback.this);
        }
    };
    View.OnClickListener btn2 = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            String t="";
            LinearLayout buttonContainer = (LinearLayout) findViewById(R.id.activity_feedback);
            for(int i=0;i<z;i++)
            {
                RatingBar r1 = (RatingBar) findViewById(i);
                t=t+r1.getRating()+",";
            }
            Toast.makeText(getApplicationContext(),t,
                    Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(con, submissions.class);
            intent.putExtra("qids",quesids);
            intent.putExtra("rollno",roll);
            intent.putExtra("ans",t);
            startActivity(intent);
//            RetrofitInterface retrofitInterface = ServiceGenerator.createService(RetrofitInterface.class);
//            retrofitInterface.sendanswers(quesids,roll,t).enqueue(feedback.this);
        }
    };

    @Override
    public void onResponse(Call<GsonModels.aa> call, Response<GsonModels.aa> response) {


        GsonModels.aa user = response.body();
        //ArrayList<String> a= ["b1","b2","b3"];
        LinearLayout buttonContainer = (LinearLayout) findViewById(R.id.activity_feedback);
        for(int i=0;i<user.questions.size();i++)
        {
            quesids = quesids + user.questions.get(i).getQuestion_id() + ",";
            LinearLayout linearLayout = (LinearLayout)findViewById(R.id.activity_feedback);
            TextView aa = new TextView(this);
            aa.setText(user.questions.get(i).getQuestion());
            linearLayout.addView(aa);
            RatingBar r1 = new RatingBar(this, null, android.R.attr.ratingBarStyle);
            r1.setNumStars(5);
            r1.setMinimumWidth(50);
            r1.setStepSize(1);
            int a= 0+i;
            r1.setId(a);
            r1.setLayoutParams(new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.WRAP_CONTENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT));
            buttonContainer.addView(r1);
            z=i+1;
        }
        //RatingBar r =(RatingBar)findViewById(i) ;

        Button button = (Button)findViewById(R.id.sub);
        //buttonContainer.addView(button);
        //button.setId(R.id.sub);
        button.setText("SUBMIT");
        button.setOnClickListener(btn2);




    }

    @Override
    public void onFailure(Call<GsonModels.aa> call, Throwable t) {
        Toast.makeText(getApplicationContext(),"ERROR",
                Toast.LENGTH_SHORT).show();
    }


}
