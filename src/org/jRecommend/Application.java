/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package org.jRecommend;

import java.util.Date;

/**
 *
 * @author akshay
 */
public class Application {
    private int userId;
    private int windowId;
    private Date applicationDate;
    private int jobId;
    
    private double jobProbability;
    private double userProbability;

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public int getWindowId() {
        return windowId;
    }

    public void setWindowId(int windowId) {
        this.windowId = windowId;
    }

    public Date getApplicationDate() {
        return applicationDate;
    }

    public void setApplicationDate(Date applicationDate) {
        this.applicationDate = applicationDate;
    }

    public int getJobId() {
        return jobId;
    }

    public void setJobId(int jobId) {
        this.jobId = jobId;
    }

    public double getJobProbability() {
        return jobProbability;
    }

    public void setJobProbability(double jobProbability) {
        this.jobProbability = jobProbability;
    }

    public double getUserProbability() {
        return userProbability;
    }

    public void setUserProbability(double userProbability) {
        this.userProbability = userProbability;
    }
    
    
}
