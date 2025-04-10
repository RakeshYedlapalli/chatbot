import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-typing-effect',
  standalone: true,
  imports: [],
  templateUrl: './typing-effect.component.html',
  styleUrl: './typing-effect.component.scss',
})
export class TypingEffectComponent implements OnInit {
  @Input()
  message: string = '';
  displayedText: string = '';
  typingSpeed: number = 10; // Adjust typing speed (milliseconds)

  ngOnInit() {
    this.typeWriter();
  }

  typeWriter(index: number = 0) {
    if (index < this.message.length) {
      this.displayedText += this.message.charAt(index);
      setTimeout(() => this.typeWriter(index + 1), this.typingSpeed);
    }
  }
}
