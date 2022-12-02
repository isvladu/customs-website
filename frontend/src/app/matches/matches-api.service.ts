import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { Match } from './match.model';

@Injectable()
export class MatchesApiService {
    constructor(private http: HttpClient) { }

    private static _handleError(err: HttpErrorResponse | any) {
        return throwError(
            () => new Error(err.message || 'Error: Unable to complete request')
        );
    }

    getMatches(): Observable<Match[]> {
        console.log(this.http.get<Match[]>(`${API_URL}/matches`));
        return this.http
            .get<Match[]>(`${API_URL}/matches`)
            .pipe(catchError(MatchesApiService._handleError));
    }
}
