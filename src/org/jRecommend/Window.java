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
public class Window {
    private Date windowStartDate;
    private Date windowEndDate;
    private double windowLength;
    
    private Date testStartDate;
    private Date testEndDate;
    private double testLength;

    private int windowId;
    
    public Date getWindowStartDate() {
        return windowStartDate;
    }

    public void setWindowStartDate(Date windowStartDate) {
        this.windowStartDate = windowStartDate;
    }

    public Date getWindowEndDate() {
        return windowEndDate;
    }

    public void setWindowEndDate(Date windowEndDate) {
        this.windowEndDate = windowEndDate;
    }

    public double getWindowLength() {
        return windowLength;
    }

    public void setWindowLength(double windowLength) {
        this.windowLength = windowLength;
    }

    public Date getTestStartDate() {
        return testStartDate;
    }

    public void setTestStartDate(Date testStartDate) {
        this.testStartDate = testStartDate;
    }

    public Date getTestEndDate() {
        return testEndDate;
    }

    public void setTestEndDate(Date testEndDate) {
        this.testEndDate = testEndDate;
    }

    public double getTestLength() {
        return testLength;
    }

    public void setTestLength(double testLength) {
        this.testLength = testLength;
    }

    public int getWindowId() {
        return windowId;
    }

    public void setWindowId(int windowId) {
        this.windowId = windowId;
    }
    
    
}
