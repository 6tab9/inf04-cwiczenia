package com.example.notatki

import android.os.Bundle
import android.widget.ArrayAdapter
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.notatki.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding:ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var notesList = listOf(
            "Zakupy: chleb, masło, ser",
            "Do zrobienia: obiad, umyć podłogi",
            "Weekend:kino,spacer z psem"
        )
        updateListView(notesList)

        binding.addNoteButton.setOnClickListener{
            notesList+=binding.newNoteTextInput.text.toString()
            updateListView(notesList)
        }
    }
    fun updateListView(updatingList:List<String>){
        val adapter = ArrayAdapter(baseContext,android.R.layout.simple_list_item_1,updatingList)
        binding.notesList.adapter=adapter
    }
}