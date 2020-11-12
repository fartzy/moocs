package io.stateoftheartz;

import static io.stateoftheartz.ThreadColor.ANSI_RED;

public class MyRunnable implements Runnable {

    @Override
    public void run() {
        System.out.println(ANSI_RED + "Hello from MyRunnable's implementation of Runnable.");
    }
}
