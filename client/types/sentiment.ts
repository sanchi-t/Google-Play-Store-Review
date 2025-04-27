
export interface SentimentRequestBody {
    appName: string;
    reviewLimit?: number | null;
  }
  
  export interface SentimentResult {
    average_score: number;
    review_count: number;
    [key: string]: any;
    app_name: string;
  }
  