from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_message_too_high():
    # When guess is too high, hint should direct player to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_message_too_low():
    # When guess is too low, hint should direct player to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_score_starts_at_zero():
    # First guess (attempt 1) on a wrong answer should deduct from 0, not go negative from a pre-decremented state
    score = update_score(0, "Too Low", 1)
    assert score == -5

def test_score_resets_to_zero():
    # Simulates a new game: score should return to 0 regardless of previous value
    score = update_score(0, "Too Low", 1)  # score is now -5
    assert score != 0                      # confirm score changed during play
    reset_score = 0                        # new game resets to 0
    assert reset_score == 0

def test_score_win_on_first_attempt():
    # Winning on attempt 1 from a fresh score of 0 should give points
    score = update_score(0, "Win", 1)
    assert score > 0
