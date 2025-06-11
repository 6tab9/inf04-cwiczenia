package com.example.myapplication

import android.os.Bundle
import android.widget.SeekBar
import android.widget.SeekBar.OnSeekBarChangeListener
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.myapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val quotes = listOf<String>(
            "Dzień dobry",
            "Good morning",
            "Buenos dias"
        )
        var quoteIndex = 0
        binding.fontSizeSlider.setOnSeekBarChangeListener(object:OnSeekBarChangeListener{
            override fun onProgressChanged(p0: SeekBar?, p1: Int, p2: Boolean) {
                binding.fontSizeText.setText("Rozmiar: ${p1}")
                binding.quoteText.textSize = p1.toFloat()
            }

            override fun onStartTrackingTouch(p0: SeekBar?) {
                var a= 0
            }

            override fun onStopTrackingTouch(p0: SeekBar?) {
                var a = 0
            }
        })
        binding.nextLanguageButton.setOnClickListener{
            if (quoteIndex < quotes.size-1){
                quoteIndex+=1
            }
            else{
                quoteIndex=0
            }
            binding.quoteText.text = quotes[quoteIndex]
        }
    }
}