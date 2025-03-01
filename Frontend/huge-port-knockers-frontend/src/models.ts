
export interface Knocker {
    ports: Port[];
    ip: string;
    failed: boolean;
}

export interface Port {
    port: number;
    correct: boolean;
}