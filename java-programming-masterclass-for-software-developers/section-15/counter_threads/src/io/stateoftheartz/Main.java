package io.stateoftheartz;


import static java.lang.Thread.currentThread;

public class Main {

    public static void main(String[] args) {

        System.out.println("Beginning: " + java.time.LocalTime.now());

        Countdown countdown = new Countdown();

        CountdownThread t1 = new CountdownThread(countdown);
        t1.setName("Thread 1");
        CountdownThread t2 = new CountdownThread(countdown);
        t2.setName("Thread 2");

        t1.start();
        t2.start();

//        try {
//            t2.join();
//            t1.join();
//        } catch (InterruptedException e) {
//            System.out.println(" " + currentThread() + " was interrupted" );
//        }

        System.out.println("Ending: " + java.time.LocalTime.now());

    }
}

class Countdown {

    private long i;

    public void doCountdown() {
        String color;

        switch(currentThread().getName()) {
            case "Thread 1":
                color = ThreadColor.ANSI_CYAN;
                break;
            case "Thread 2":
                color = ThreadColor.ANSI_PURPLE;
                break;
            default:
                color = ThreadColor.ANSI_GREEN;
        }

        synchronized (Countdown.class) {

            for (i = 10; i > 0; i--) {
                System.out.println(color + currentThread().getName() + ": i =" + i );
            }

        }
    }
}

class CountdownThread extends Thread{
    private Countdown threadCountdown;

    public CountdownThread(Countdown countdown){
        threadCountdown = countdown;
    }

    public void run() {
        threadCountdown.doCountdown();
    }
}