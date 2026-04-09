from .players.elves.elf_ranger import ElfRanger
from .players.elves.druid import Druid
from .players.dwarves.dwarf_warrior import DwarfWarrior
from .players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf
from .players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )

    druid = Druid(
        nickname="Elrond",
        musical_instrument="harp",
        favourite_spell="Fire Storm"
    )

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )

    blacksmith = DwarfBlacksmith(
        nickname="Thorin",
        favourite_dish="Stew",
        skill_level=9
    )

    print(ranger.get_rating())
    print(ranger.player_info())
    ranger.play_elf_song()

    print(druid.get_rating())
    print(druid.player_info())
    druid.play_elf_song()

    print(warrior.get_rating())
    print(warrior.player_info())
    warrior.eat_favourite_dish()

    print(blacksmith.get_rating())
    print(blacksmith.player_info())
    blacksmith.eat_favourite_dish()
