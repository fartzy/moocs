package io.stateoftheartz;

import static io.stateoftheartz.ThreadColor.*;
import static java.lang.Thread.currentThread;

public class Main {

    public static void main(String[] args) {

	    System.out.println(ANSI_PURPLE + "Hello from the main thread.");

	    Thread anotherThread = new AnotherThread();
	    anotherThread.setName("== Another Thread ==");
	    anotherThread.start();

	    new Thread() {
	    	public void run() {
	    		System.out.println(ANSI_GREEN + "Hello from the anonymous class thread.");
			}
		}.start();

	    Thread myRunnableThread = new Thread(new MyRunnable());
	    myRunnableThread.start();

	    Thread anotherMyRunnableThread = new Thread(new MyRunnable() {
	    	@Override
			public void run() {
	    		System.out.println(ANSI_RED + "Hello from the anonymous class's implementation of run.");
	    		try {
	    			anotherThread.join();
	    			System.out.println(ANSI_RED + "Another Thread terminated, or timed out, so " + currentThread().getName() + " is running again.");
				} catch(InterruptedException e) {
	    			System.out.println(ANSI_RED + "I couldn't wait after all. I was interrupted");
				}
			}
		});

		anotherMyRunnableThread.start();

	    System.out.println(ANSI_PURPLE + "Hello again from the main thread.");

    }
}
