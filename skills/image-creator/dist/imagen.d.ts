import { GoogleGenAI } from "@google/genai";
export declare function resolveApiKey(): string;
export declare function createClient(apiKey: string): GoogleGenAI;
export declare function enhancePrompt(client: GoogleGenAI, theme: string, style: string, context?: string): Promise<string>;
export interface GenerateImageOptions {
    engine?: string;
    aspectRatio?: string;
    format?: string;
}
export declare function generateImage(client: GoogleGenAI, prompt: string, options?: GenerateImageOptions): Promise<Buffer>;
