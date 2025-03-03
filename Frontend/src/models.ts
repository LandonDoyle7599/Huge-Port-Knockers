
export type KnockerMap = Map<string, Knocker>;
export interface Knocker {
    ip: string;
    failed: boolean;
    ports: Port[];
    connected: boolean;
}

export interface Port {
    port: number;
    correct: boolean;
}