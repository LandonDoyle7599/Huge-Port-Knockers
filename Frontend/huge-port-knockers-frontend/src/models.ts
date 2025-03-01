export interface Knocker {
    ip: string;
    ports: KnockerPort[];
    failed: boolean;
}

export interface KnockerTableModel {
    knockers: Knocker[];
}

export interface KnockerPort {
    port: number;
    correct: boolean;
}