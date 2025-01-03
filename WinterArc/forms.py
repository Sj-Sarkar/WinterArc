from django import forms
from .models import Scorecard

class ScorecardForm(forms.ModelForm):
    class Meta:
        model = Scorecard
        fields = ['match', 'player', 'innings', 'runs', 'balls', 'how_out', 'overs', 'wickets', 'runs_conceded', 'submitted']
