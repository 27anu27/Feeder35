package com.bhatore.android.feeder35;

import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

public interface RetrofitInterface {
    //int a=150020086;
    @FormUrlEncoded
    @POST("/login/android/")
    Call<GsonModels.UserDetails> getUserDetails(@Field("username") String username, @Field("password") String password);
    @FormUrlEncoded
    @POST("/login/courses/")
    Call<GsonModels.Details> getString(@Field("username") String username);
    @FormUrlEncoded
    @POST("/login/question/")
    Call<GsonModels.aa> send(@Field("response_id") String username,@Field("student_id") String pass);
    @FormUrlEncoded
    @POST("/login/answer/")
    Call<GsonModels.result> sendanswers(@Field("ques_id") String username,@Field("student_id") String pass,@Field("answer") String hello);
}
