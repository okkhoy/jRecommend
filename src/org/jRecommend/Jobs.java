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
public class Jobs {
    private int jobId;
    private int windowId;
    private String title;
    private Degree requirement;
    private String city;
    private String state;
    private String country;
    private String zip;
    private Date startDate;
    private Date endDate;
    
    private float windowProbability;
    private float jobProbability;

    public int getJobId() {
        return jobId;
    }

    public void setJobId(int jobId) {
        this.jobId = jobId;
    }

    public int getWindowId() {
        return windowId;
    }

    public void setWindowId(int windowId) {
        this.windowId = windowId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Degree getRequirement() {
        return requirement;
    }

    public void setRequirement(Degree requirement) {
        this.requirement = requirement;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }

    public Date getStartDate() {
        return startDate;
    }

    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public void setEndDate(Date endDate) {
        this.endDate = endDate;
    }

    
    public float getWindowProbability() {
        return windowProbability;
    }

    public void setWindowProbability(float windowProbability) {
        this.windowProbability = windowProbability;
    }

    public float getJobProbability() {
        return jobProbability;
    }

    public void setJobProbability(float jobProbability) {
        this.jobProbability = jobProbability;
    }
    
    
}   
