export interface Knocker {
    ip: string;
    ports: KnockerPort[];
    authenticated: boolean;
}

export interface KnockerTableModel {
    knockers: Knocker[];
}

export interface KnockerPort {
    port: number;
    correct: boolean;
}