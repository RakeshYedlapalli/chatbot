import { TestBed } from '@angular/core/testing';
import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';
import { ChatBotService } from './chat-bot.service';
import { ChatMessage } from '../models/message';

describe('ChatBotService', () => {
  let service: ChatBotService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [ChatBotService],
    });
    service = TestBed.inject(ChatBotService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify(); // Ensure no outstanding HTTP requests
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should send a POST request to get a response', () => {
    const mockResponse: ChatMessage = {
      text: 'Hello, how can I help you?',
      sender: 'bot',
    };
    const testMessage = 'Hi';

    service.getResponse(testMessage).subscribe((response) => {
      expect(response).toEqual(mockResponse);
    });

    const req = httpMock.expectOne('http://localhost:5000/ask');
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual({ question: testMessage });
    req.flush(mockResponse); // Simulate the server response
  });
});
