import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ChatMessage } from '../models/message';

@Injectable({
  providedIn: 'root',
})
export class ChatBotService {
  constructor(private _httpClient: HttpClient) {}

  getResponse(message: string) {
    return this._httpClient.post<ChatMessage>('http://localhost:5000/ask', {
      question: message,
    });
  }
}
