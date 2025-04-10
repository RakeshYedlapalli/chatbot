import { CommonModule } from '@angular/common';
import {
  ChangeDetectorRef,
  Component,
  ElementRef,
  inject,
  OnDestroy,
  OnInit,
  ViewChild,
} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatTooltipModule } from '@angular/material/tooltip';
import { Subject } from 'rxjs';
import { ChatMessage } from '../../models/message';
import { ChatBotService } from '../../services/chat-bot.service';
import { TypingEffectComponent } from '../typing-effect/typing-effect.component';

@Component({
  selector: 'app-landing-page',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatButtonModule,
    MatInputModule,
    MatCardModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatIconModule,
    MatTooltipModule,
    TypingEffectComponent,
  ],
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.scss',
})
export class LandingPageComponent implements OnInit, OnDestroy {
  messages: ChatMessage[] = [];
  input = '';
  isLoading = false;
  @ViewChild('messagesEnd') messagesEndRef!: ElementRef;
  @ViewChild('inputField') inputField!: ElementRef<HTMLInputElement>;
  private destroy$ = new Subject<void>();

  private _chatBotService = inject(ChatBotService);
  constructor(private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.inputField?.nativeElement.focus();
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  handleSendMessage(): void {
    if (!this.input.trim()) return;

    const userMessage: ChatMessage = { text: this.input, sender: 'user' };
    this.messages = [...this.messages, userMessage];
    this.input = '';
    this.isLoading = true;

    this._chatBotService.getResponse(userMessage.text).subscribe({
      next: (response) => {
        const botMessage: ChatMessage = { text: response.text, sender: 'bot' };
        this.messages = [...this.messages, botMessage];
      },
      error: (error) => {
        console.error('Failed to get response:', error);
        const errorMessage: ChatMessage = {
          text: "Sorry, I couldn't process your request. Please try again.",
          sender: 'bot',
        };
        this.messages = [...this.messages, errorMessage];
      },
      complete: () => {
        this.isLoading = false;
        this.cdr.detectChanges(); // Manually trigger change detection
      },
    });
  }

  handleInputChange(event: Event): void {
    this.input = (event.target as HTMLInputElement).value;
  }

  handleKeyDown(): void {
    this.handleSendMessage();
  }

  handleNewChat(): void {
    this.messages = [];
    this.input = '';
    this.isLoading = false;
  }

  ngAfterViewChecked(): void {
    this.scrollToBottom();
  }

  scrollToBottom(): void {
    try {
      this.messagesEndRef.nativeElement.scrollIntoView({ behavior: 'smooth' });
    } catch (err) {}
  }
}
