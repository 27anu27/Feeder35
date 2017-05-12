package com.bhatore.android.feeder35;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.FragmentTransaction;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.roomorama.caldroid.CaldroidFragment;
import com.roomorama.caldroid.CaldroidListener;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

import static com.bhatore.android.feeder35.GsonModels.*;

public class studentmain extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener , Callback<GsonModels.Details> {
    GsonModels.Details userDetails;
    final Activity context1  =  this;
    TextView textView;
    final Map<Date, Drawable> backgroundForDateMap = new HashMap<>();
    final Calendar c = Calendar.getInstance();
    String roll ="150050055";
    CaldroidFragment caldroidFragment;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_studentmain);

        //Retrieve a value from SharedPreference
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

//        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
//            }
//        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        final SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
        setnavigationbar(sharedPreference.getValue(),sharedPreference.getEmail());
        final CaldroidListener listener = setcalendarlistener();
        //test
        caldroidFragment = new CaldroidFragment();
        Bundle args = new Bundle();
        Calendar cal = Calendar.getInstance();
        args.putInt(CaldroidFragment.MONTH, cal.get(Calendar.MONTH) + 1);
        args.putInt(CaldroidFragment.YEAR, cal.get(Calendar.YEAR));
        caldroidFragment.setArguments(args);

        FragmentTransaction t = getSupportFragmentManager().beginTransaction();
        t.replace(R.id.calendar1, caldroidFragment);
        t.commit();

        caldroidFragment.setCaldroidListener(listener);

        //String subdate = "Divyansh";
        //NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        View header=navigationView.getHeaderView(0);
        TextView name =(TextView)header.findViewById(R.id.studentname);
        RetrofitInterface retrofitInterface = ServiceGenerator.createService(RetrofitInterface.class);
        retrofitInterface.getString(name.getText().toString()).enqueue(studentmain.this);

    }

    private void setlistitems(final List<Try> aa,int z) {
        final String[] mobileArray = new String[z];
        for(int i=0;i<z;i++)
        {
            mobileArray[i] = aa.get(i).getType();
        }
        ArrayAdapter adapter = new ArrayAdapter<String>(this, R.layout.list_view, mobileArray);
        ListView listView = (ListView) findViewById(R.id.mobile_list);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> a, View v, int position, long id) {
                Intent intent = new Intent(context1, feedback.class);
                Try pressed = aa.get(position);
                //final SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
                NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
                View header=navigationView.getHeaderView(0);
                TextView name =(TextView)header.findViewById(R.id.studentname);
                intent.putExtra("stud",name.getText());
                intent.putExtra("type",pressed.getType());
                intent.putExtra("date",pressed.Sub_date);
                intent.putExtra("course",pressed.course);
                intent.putExtra("id",pressed.id);
                intent.putExtra("feedback",pressed.feedback);
                startActivity(intent);
            }
        });
    }


    private CaldroidListener setcalendarlistener() {
        CaldroidListener listener = new CaldroidListener() {
            DateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
            @Override
            public void onSelectDate(Date date, View view) {
                Toast.makeText(getApplicationContext(), formatter.format(date),
                        Toast.LENGTH_SHORT).show();
                //mylist.clear();
                int z=0;
//                if(userDetails.coursesList.isEmpty())
                    //return;
                ArrayList<Try> mylist = new ArrayList<Try>();
                String f = formatter.format(date);
                for(int i=0;i<userDetails.coursesList.size();i++)
                {
                    for(int j=0;j<userDetails.coursesList.get(i).deadlines.size();j++)
                    {
                        String t =userDetails.coursesList.get(i).deadlines.get(j).getDate();

                        if(t.equals(f))
                        {
                            Try a = new Try();
                            a.Sub_date = formatter.format(date);
                            a.id = userDetails.coursesList.get(i).deadlines.get(j).getId();
                            a.feedback = "0";
                            a.type = userDetails.coursesList.get(i).deadlines.get(j).getType();
                            a.course = userDetails.coursesList.get(i).course_name+" - "+userDetails.coursesList.get(i).course_code;
                            mylist.add(a);
                            z=z+1;
                        }
                    }
                }
                for(int i=0;i<userDetails.coursesList.size();i++)
                {
                    for(int j=0;j<userDetails.coursesList.get(i).feedbacks.size();j++)
                    {
                        String t =userDetails.coursesList.get(i).feedbacks.get(j).getFeedback_date();
                        if(t.equals(f))
                        {
                            Try a = new Try();
                            a.Sub_date = formatter.format(date);
                            a.id = userDetails.coursesList.get(i).feedbacks.get(j).getFeedback_id();
                            a.feedback = "1";
                            a.type = userDetails.coursesList.get(i).feedbacks.get(j).getFeedback_type();
                            a.course = userDetails.coursesList.get(i).course_name+" - "+userDetails.coursesList.get(i).course_code;
                            mylist.add(a);
                            z=z+1;
                        }
                    }
                }
                setlistitems(mylist,z);

            }

        };
        return listener;
    }

    private void setnavigationbar(String n,String e) {
        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        View header=navigationView.getHeaderView(0);
        TextView name =(TextView)header.findViewById(R.id.studentname);
        name.setText(n);
        TextView email = (TextView)header.findViewById(R.id.studentemail);
        email.setText(e);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            //super.onBackPressed();
            Toast.makeText(this,"Disabled! Logout from the drawer.",Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.studentmain, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {

        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.logoutdrawer) {
            logoutapp();

        } else if (id == R.id.switchaccdrawer) {
            logoutapp();
        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
    public void logoutapp()   {
        final SharedPreference sharedPreference = new SharedPreference(getApplicationContext());
        sharedPreference.clearSharedPreference();
        finish();
        Intent i = new Intent(studentmain.this,loginpage.class);
        startActivity(i);
    }

    @Override
    public void onResponse(Call<GsonModels.Details> call, Response<GsonModels.Details> response) {
        if(response.isSuccessful()) {

            userDetails = response.body();
            Toast.makeText(this,userDetails.toString(),Toast.LENGTH_SHORT).show();
            SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
            for(int i=0;i<userDetails.coursesList.size();i++)
            {
                for(int j=0;j<userDetails.coursesList.get(i).deadlines.size();j++)
                {
                    try{
                    backgroundForDateMap.put(format.parse(userDetails.coursesList.get(i).deadlines.get(j).getDate()), new ColorDrawable(Color.GREEN));}catch (ParseException e){}
                }
            }
            for(int i=0;i<userDetails.coursesList.size();i++)
            {
                for(int j=0;j<userDetails.coursesList.get(i).feedbacks.size();j++)
                {
                    try{
                        backgroundForDateMap.put(format.parse(userDetails.coursesList.get(i).feedbacks.get(j).getFeedback_date()), new ColorDrawable(Color.YELLOW));}catch (ParseException e){}
                }
            }
            caldroidFragment.setBackgroundDrawableForDates(backgroundForDateMap);
            caldroidFragment.refreshView();
        }
        else {
            Toast.makeText(this,"Response Code: "+String.valueOf(response.code()),Toast.LENGTH_SHORT).show();
        }
    }
    @Override
    public void onFailure(Call<GsonModels.Details> call, Throwable t) {
        Toast.makeText(this,"Error",Toast.LENGTH_SHORT).show();
    }


    public class Try
    {
        public String feedback;
        public String Sub_date;
        public String type;
        public String id;
        public String course;
        Try()
        {
            super();
        }

        public String getType() {
            return type;
        }
    }



}
