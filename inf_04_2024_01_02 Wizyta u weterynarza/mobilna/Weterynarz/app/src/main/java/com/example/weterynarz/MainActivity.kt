package com.example.weterynarz

import android.content.DialogInterface
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.AdapterView.OnItemClickListener
import android.widget.SeekBar
import android.widget.SeekBar.OnSeekBarChangeListener
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.weterynarz.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding:ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        var zwierze = ""
        binding.gatunkiList.setOnItemClickListener(object:OnItemClickListener{
            override fun onItemClick(p0: AdapterView<*>?, p1: View?, p2: Int, p3: Long) {
                when(p2){
                    0->{
                        zwierze = "Pies"
                        binding.ageSeekBar.max = 18
                    }
                    1->{
                        zwierze = "Kot"
                        binding.ageSeekBar.max = 20
                    }
                    2->{
                        zwierze = "Świnka morska"
                        binding.ageSeekBar.max = 9
                    }
                }
            }

        })
        binding.ageSeekBar.setOnSeekBarChangeListener(object:OnSeekBarChangeListener{
            override fun onProgressChanged(p0: SeekBar?, p1: Int, p2: Boolean) {
                binding.ageOutput.text = "Ile ma lat? ${p1}"
            }

            override fun onStartTrackingTouch(p0: SeekBar?) {
                var a = 0
            }

            override fun onStopTrackingTouch(p0: SeekBar?) {
                var a = 0
            }

        })
        binding.okButton.setOnClickListener{
            val alertDialogBuilder = AlertDialog.Builder(baseContext)
                .setTitle("Zapisana wizyta")
                .setMessage("${binding.wlascicielInput}. ${zwierze}, ${binding.ageSeekBar.progress}, ${binding.celWizytyInput}, ${binding.czasInput}")
                .setCancelable(true)
                .setPositiveButton("Ok") { dialogInterface, i ->
                    dialogInterface.cancel()
                }

            alertDialogBuilder.show()
        }
    }
}