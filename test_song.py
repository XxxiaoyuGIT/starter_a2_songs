"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    print("\nTest initial-value song:")
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    assert initial_song.title == "My Happiness"
    assert initial_song.artist == "Powderfinger"
    assert initial_song.year == 1996
    assert initial_song.is_learned

    # Test mark_as_learned and mark_as_unlearned methods
    print("\nTest mark_as_learned and mark_as_unlearned methods:")
    unlearned_song = Song("Unlearned Song", "Unknown Artist", 2000)
    print(f"Before learning: {unlearned_song}")
    assert not unlearned_song.is_learned

    # Mark the song as unlearned
    unlearned_song.mark_as_unlearned()
    print(f"After unlearning: {unlearned_song}")
    assert not unlearned_song.is_learned

    # Mark the song as learned
    unlearned_song.mark_as_learned()
    print(f"After learning: {unlearned_song}")
    assert unlearned_song.is_learned

run_tests()