const BACKEND_HOST = process.env.NEXT_PUBLIC_BACKEND_HOST || "127.0.0.1";
const BACKEND_PORT = process.env.NEXT_PUBLIC_BACKEND_PORT || "8000";

export const BACKEND_URL = `http://${BACKEND_HOST}:${BACKEND_PORT}`;
