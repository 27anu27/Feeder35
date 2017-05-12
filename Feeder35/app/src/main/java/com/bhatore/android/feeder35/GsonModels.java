package com.bhatore.android.feeder35;

import java.util.ArrayList;
import java.util.List;

public class GsonModels {
    public class result{
        String res;

        public void setRes(String res) {
            this.res = res;
        }
    }

    public class aa
    {
        ArrayList<Questions> questions;

        public void setQuestions(ArrayList<Questions> questions) {
            for(int i=0;i<questions.size();i++)
            {
                Questions a;
                a=questions.get(i);
                this.questions.add(a);
            }
        }
    }

    public class UserDetails {
        private int name;
        private String rollno;
        private String email;
        private boolean loggedin;

        public String getName() {
            return String.valueOf(name);
        }

        public void setName(int name) {
            this.name = name;
        }

        public void setloggedin(boolean a) {
            this.loggedin = a;
        }

        public boolean getloggedin() {
            return loggedin;
        }

        public String getRollno() {
            return rollno;
        }

        public void setRollno(String rollno) {
            this.rollno = rollno;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public UserDetails(int name, String rollno, String email, boolean loggedin) {

            this.name = name;
            this.rollno = rollno;
            this.email = email;
            this.loggedin = loggedin;
        }
    }

    public class Deadlines {
        String Sub_date;
        String id;
        String type;

        public void setDate(String date) {
            Sub_date = date;
        }

        public void setId(String id) {
            this.id = id;
        }

        public void setType(String type) {
                this.type = type;
        }

        public String getId() {
            return id;
        }

        public String getDate() {
            return Sub_date;
        }

        public String getType() {
            return type;
        }

        @Override
        public String toString() {
            return Sub_date+id+type;
        }
    }

    public class Questions{
        String question_id;
        String question;

        public void setQuestion(String question) {
            this.question = question;
        }

        public void setQuestion_id(String question_id) {
            this.question_id = question_id;
        }

        public String getQuestion_id() {
            return question_id;
        }

        public String getQuestion() {
            return question;
        }
    }

    public class Feedbacks{
        public String feedback_id;
        public String feedback_date;
        public String feedback_type;
        //ArrayList<Questions> questions;

        public void setFeedback_date(String feedback_date) {
            this.feedback_date = feedback_date;
        }

        public void setFeedback_id(String feedback_id) {
            this.feedback_id = feedback_id;
        }

        public void setFeedback_type(String feedback_type) {
            this.feedback_type = feedback_type;
        }

        public String getFeedback_date() {
            return feedback_date;
        }

        public String getFeedback_id() {
            return feedback_id;
        }

        public String getFeedback_type() {
            return feedback_type;
        }


    }

    public class Courses {
        String course_instructor;
        String course_venue;
        String course_slot;
        String course_name;
        String course_code;
        String course_sem;
//        boolean course_halfsem;
        String course_credit;
        ArrayList<Deadlines> deadlines;
        ArrayList<Feedbacks> feedbacks;

        public void setCourse_code(String course_code) {
            this.course_code = course_code;
        }

        public void setCourse_venue(String course_venue) {
            this.course_venue = course_venue;
        }

        public void setCourse_slot(String course_slot) {
            this.course_slot = course_slot;
        }

        public void setCourse_sem(String course_sem) {
            this.course_sem = course_sem;
        }

        public void setCourse_name(String course_name) {
            this.course_name = course_name;
        }

        public void setCourse_instructor(String course_instructor) {
            this.course_instructor = course_instructor;
        }

//        public void setCourse_halfsem(boolean course_halfsem) {
//            this.course_halfsem = course_halfsem;
//        }

        public void setCourse_credit(String course_credit) {
            this.course_credit = course_credit;
        }

        public void setDeadlines(ArrayList<Deadlines> deadlines) {
            for (int i=0;i<deadlines.size();i++)
            {
                Deadlines a;
                a= deadlines.get(i);
                this.deadlines.add(a);
            }
        }

        public void setFeedbacks(ArrayList<Feedbacks> feedbacks) {
            for (int i=0;i<feedbacks.size();i++)
            {
                Feedbacks a;
                a=feedbacks.get(i);
                this.feedbacks.add(a);
            }
        }

        @Override
        public String toString() {
            String t="";
            for(int i=0;i<deadlines.size();i++)
            {
                t =t+deadlines.toString();
            }

            return t;
        }

    }

    public class Details {
        public ArrayList<Courses> coursesList;

        public void setCoursesList(List<Courses> coursesList) {
            for (int i=0;i<coursesList.size();i++)
            {
                System.out.println(coursesList.size());
                Courses a ;
                a=coursesList.get(i);
                this.coursesList.add(a);
            }
        }

        @Override
        public String toString() {
            String t="";
            for(int i=0;i<coursesList.size();i++)
            {
                t = t+ coursesList.get(i).toString();
            }
            return t;
        }

    }

}
