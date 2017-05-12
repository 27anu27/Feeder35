package com.bhatore.android.feeder35;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;

public class SharedPreference {
    public static String username = "Username";
    public static String  email= "Password";
    public static String roll = "150050055";
    public static String loggedin = "0";
    public SharedPreferences settings;
    public Editor editor;
    public Context _context;
    public SharedPreference(Context context) {
        super();
        this._context = context;
        settings = _context.getSharedPreferences("abcd",Context.MODE_PRIVATE);
        editor = settings.edit();
    }

    public void save(String text,String pass,String rol) {

        //settings = PreferenceManager.getDefaultSharedPreferences(context);
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE); //1
        editor = settings.edit(); //2

        editor.putString(email, pass); //3
        editor.putString(username, text);
        editor.putString(loggedin, "hi");
        editor.putString(roll,rol);
        editor.commit(); //4
    }

    public String getValue() {
        String text;

        //settings = PreferenceManager.getDefaultSharedPreferences(context);
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE);
        text = settings.getString(username, null);
        return text;
    }
    public void setnull() {

        //settings = PreferenceManager.getDefaultSharedPreferences(context);
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE); //1
        editor = settings.edit(); //2
        editor.putString(loggedin, "0");

        editor.commit(); //4
    }
    public String getEmail() {
        String text;

        //settings = PreferenceManager.getDefaultSharedPreferences(context);
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE);
        text = settings.getString(email, null);
        return text;
    }
    public String getLoggedin() {
        String text;

        //settings = PreferenceManager.getDefaultSharedPreferences(context);
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE);
        text = settings.getString(loggedin, "0");
        return text;
    }

    public String getRoll() {
        int text;
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE);
        text = settings.getInt(roll,1500);
        return String.valueOf(text);
    }

    public void clearSharedPreference() {

        //settings = PreferenceManager.getDefaultSharedPreferences(context);
        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE);
        editor = settings.edit();

        editor.clear();
        editor.putString(loggedin,"0");
        editor.commit();
    }

    public void removeValue() {

        settings = _context.getSharedPreferences("abcd", Context.MODE_PRIVATE);
        editor = settings.edit();

        editor.putString(loggedin,"0");
        editor.commit();
    }

}
