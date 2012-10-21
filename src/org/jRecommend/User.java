/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package org.jRecommend;

/**
 *
 * @author akshay
 */
public class User {
    private int userId;
    private int windowId;
    private String state;
    private String city;
    private String country;
    private String zipCode;
    private Degree degree;
    private int workHistoryCount;
    private int totalExperience;
    private boolean currentlyEmployed;
    private boolean managedOthers;
    private int subordinatesCount;
    
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

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getZipCode() {
        return zipCode;
    }

    public void setZipCode(String zipCode) {
        this.zipCode = zipCode;
    }

    public Degree getDegree() {
        return degree;
    }

    public void setDegree(Degree degree) {
        this.degree = degree;
    }

    public int getWorkHistoryCount() {
        return workHistoryCount;
    }

    public void setWorkHistoryCount(int workHistoryCount) {
        this.workHistoryCount = workHistoryCount;
    }

    public int getTotalExperience() {
        return totalExperience;
    }

    public void setTotalExperience(int totalExperience) {
        this.totalExperience = totalExperience;
    }

    public boolean isCurrentlyEmployed() {
        return currentlyEmployed;
    }

    public void setCurrentlyEmployed(boolean currentlyEmployed) {
        this.currentlyEmployed = currentlyEmployed;
    }

    public boolean isManagedOthers() {
        return managedOthers;
    }

    public void setManagedOthers(boolean managedOthers) {
        this.managedOthers = managedOthers;
    }

    public int getSubordinatesCount() {
        return subordinatesCount;
    }

    public void setSubordinatesCount(int subordinatesCount) {
        this.subordinatesCount = subordinatesCount;
    }
    
    
}
