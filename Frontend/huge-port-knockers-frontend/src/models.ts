export interface Knocker {
    
}

export interface KnockerTableModel {
    knockers: Knocker[];
}

export interface KnockerPort {
    port: number;
    correct: boolean;
}