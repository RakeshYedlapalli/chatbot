// import { ComponentFixture, TestBed } from '@angular/core/testing';
// import { LandingPageComponent } from './landing-page.component';
// import { ChatBotService } from '../../services/chat-bot.service';
// import { HttpClientTestingModule } from '@angular/common/http/testing';
// import { of } from 'rxjs';

// interface ChatMessage {
//   text: string;
//   sender: 'user' | 'bot';
// }

// describe('LandingPageComponent', () => {
//   let component: LandingPageComponent;
//   let fixture: ComponentFixture<LandingPageComponent>;
//   let chatBotServiceSpy: jasmine.SpyObj<ChatBotService>;

//   beforeEach(async () => {
//     const spy = jasmine.createSpyObj('ChatBotService', ['getResponse']);

//     await TestBed.configureTestingModule({
//       imports: [HttpClientTestingModule, LandingPageComponent],
//       declarations: [],
//       providers: [{ provide: ChatBotService, useValue: spy }],
//     }).compileComponents();

//     fixture = TestBed.createComponent(LandingPageComponent);
//     component = fixture.componentInstance;
//     chatBotServiceSpy = TestBed.inject(
//       ChatBotService
//     ) as jasmine.SpyObj<ChatBotService>;
//     fixture.detectChanges();
//   });

//   it('should create the component', () => {
//     expect(component).toBeTruthy();
//   });

//   // it('should send a message and add it to the messages array', () => {
//   //   const userMessage = 'Hello';
//   //   const botResponse: ChatMessage = {
//   //     text: 'Hi there!',
//   //     sender: 'bot' as 'bot',
//   //   };

//   //   chatBotServiceSpy.getResponse.and.returnValue(of(botResponse));

//   //   component.input = userMessage;
//   //   component.handleSendMessage();

//   //   expect(component.messages.length).toBe(2);
//   //   expect(component.messages[0].text).toBe(userMessage);
//   //   expect(component.messages[1].text).toBe(botResponse.text);
//   //   expect(chatBotServiceSpy.getResponse).toHaveBeenCalledWith(userMessage);
//   // });

//   // it('should not send a message if input is empty', () => {
//   //   component.input = '';
//   //   component.handleSendMessage();

//   //   expect(component.messages.length).toBe(0);
//   //   expect(chatBotServiceSpy.getResponse).not.toHaveBeenCalled();
//   // });

//   // it('should clear messages and reset input on handleNewChat', () => {
//   //   component.messages = [{ text: 'Test message', sender: 'user' }];
//   //   component.input = 'Test input';

//   //   component.handleNewChat();

//   //   expect(component.messages.length).toBe(0);
//   //   expect(component.input).toBe('');
//   // });
// });
