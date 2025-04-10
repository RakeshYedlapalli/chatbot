// import {
//   animate,
//   state,
//   style,
//   transition,
//   trigger,
// } from '@angular/animations';

// // BASE URL for API requests
// export const BASE_URL = 'localhost:3000'; // Update with your actual base URL

// // Placeholder for actual chatbot integration (replace with real logic)
// export const simulateChatResponse = (message: string): Promise<string> => {
//   return new Promise((resolve) => {
//     const responses = [
//       'Hello! How can I assist you today?',
//       "I'm here to help with your queries.",
//       "That's an interesting question!",
//       'Please provide more details so I can assist you better.',
//       'I can guide you through our services.',
//       "Our documentation might have the answer you're looking for.",
//       "I'm still under development, but I'm learning quickly!",
//       'Thanks for your feedback!',
//       'How can I help you get started?',
//       'What features are you most interested in?',
//     ];
//     const randomResponse =
//       responses[Math.floor(Math.random() * responses.length)];
//     setTimeout(() => {
//       resolve(randomResponse);
//     }, 500 + Math.random() * 1000); // Simulate network latency
//   });
// };
// // Animation variants (Angular)
// export const messageVariants = [
//   trigger('messageAnimation', [
//     state('hidden', style({ opacity: 0, transform: 'translateY(20px)' })),
//     state('visible', style({ opacity: 1, transform: 'translateY(0)' })),
//     transition('hidden => visible', animate('300ms')),
//     transition('visible => hidden', animate('200ms')),
//   ]),
// ];

// export const cardVariants = [
//   trigger('cardAnimation', [
//     state('hidden', style({ opacity: 0, scale: 0.95 })),
//     state('visible', style({ opacity: 1, scale: 1 })),
//     transition('hidden => visible', animate('400ms ease-in-out')),
//     transition('visible => hidden', animate('200ms')),
//   ]),
// ];
