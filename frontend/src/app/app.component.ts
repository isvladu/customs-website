import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { MatchesApiService } from './matches/matches-api.service';
import { Match } from './matches/match.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  matchesListSubs!: Subscription;
  matchesList!: Match[];

  constructor(private matchesApi: MatchesApiService) {

  }

  ngOnInit(): void {
    this.matchesListSubs = this.matchesApi.getMatches().subscribe(res => {
      this.matchesList = res;
    },
      console.error
    );
  }

  ngOnDestroy(): void {
    this.matchesListSubs.unsubscribe();
  }
}
