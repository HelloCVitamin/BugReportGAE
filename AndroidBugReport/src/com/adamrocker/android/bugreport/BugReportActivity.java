package com.adamrocker.android.bugreport;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class BugReportActivity extends Activity {

	@Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Thread.setDefaultUncaughtExceptionHandler(new MyUncaughtExceptionHandler(this));
        setContentView(R.layout.main);
        Button oobBtn = (Button)findViewById(R.id.oob_btn);
        oobBtn.setOnClickListener(new View.OnClickListener(){
			public void onClick(View v) {
		    	int index = 5;
		    	String[] strs = new String[index];
		    	String str = strs[index];//ここでIndexOutOfBoundsException
			}});
    }
	
	public void onStart(){
		super.onStart();
		//前回バグで強制終了した場合はダイアログ表示
		MyUncaughtExceptionHandler.showBugReportDialogIfExist();
	}
}