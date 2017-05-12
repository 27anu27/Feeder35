package com.bhatore.android.feeder35;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button b1 = (Button) findViewById( R.id.b1 );
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent myIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://192.168.43.69:8090/admin/login/?next=/admin/"));
                startActivity(myIntent);
            }
        });

        Button b2 = (Button) findViewById( R.id.b2 );
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i=new Intent(MainActivity.this,loginpage.class);
                startActivity(i);

            }
        });
    }
}
