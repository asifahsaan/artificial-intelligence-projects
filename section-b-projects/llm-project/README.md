# 🧠 Companion Builder (Converso) – AI-Powered LMS SaaS

## Student Names
- Syed Laeeq Ahmed – 70125188  
- Shanzay Javed – 70137114  
- Haroon Qadeer – 70135512  
- Malaika Fatima – 70137332  

## Problem Statement
Converso is a full-stack AI-powered Learning Management System (LMS) SaaS platform that allows users to create, customize, and interact with AI voice companions. The platform addresses the need for personalized, interactive learning experiences by combining AI assistants with modern web technology for real-time engagement, tutoring, and skill development.

## Dataset / Resources
- No specific dataset; uses AI models via **Vapi AI** for voice and conversational intelligence.  
- Supabase for backend storage and real-time data sync.  
- Third-party APIs and tools: Stripe (billing), Clerk (authentication).

## Model / Technique Used
- **Vapi AI** – TTS + STT + conversational AI for real-time learning agents  
- **LLM integration** – Natural language interaction and tutoring  
- Next.js 14 + TypeScript – Full-stack web framework  
- Supabase – Database & real-time backend  
- Clerk – Authentication management  
- Tailwind CSS + shadcn/ui – UI components and styling  

## Features
- 🎙️ **Voice AI Tutors** – Custom AI companions trained on selected topics/subjects  
- 👤 **Authentication & Sessions** – Secure sign-in via Clerk & Google OAuth  
- 💳 **Subscription Plans** – Stripe-powered billing and gated content access  
- 🧠 **Tutor Builder** – Configure AI companions’ voice, subject, and style  
- 📚 **Bookmarks & History** – Save sessions and resume later  
- 🔎 **Search & Filter** – Quick lookup of topics, subjects, or companion names  
- 📦 **Reusable Components** – Modular Next.js + shadcn/ui architecture  
- ⚡ **Real-time & Scalable** – Supabase backend for data sync  
- 📱 **Fully Responsive** – Seamless experience on mobile, tablet, and desktop  

## Tech Stack
| Technology | Role |
|------------|------|
| Next.js 14 | Full-stack React framework, SSR, routing, API |
| TypeScript | Type safety |
| Supabase | Database, authentication, file storage |
| Clerk | User authentication & sessions |
| Stripe | Billing and subscription management |
| Vapi AI | Voice agent SDK (TTS + STT + conversational AI) |
| Tailwind CSS | Responsive UI |
| shadcn/ui | Component system built on Radix UI |
| Zod | Schema validation (frontend + backend) |
| Sentry | Error logging & monitoring |

## How to Run
### Prerequisites
- Node.js 18+  
- npm  
- Git  

### Project Repository
The full project is hosted at: [LLM-Saas GitHub Repository](https://github.com/LaeeqtheDev/LLM-Saas)

### Clone the Repo
```bash
git clone https://github.com/LaeeqtheDev/LLM-Saas.git
cd companion-builder
