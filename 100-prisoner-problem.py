import random
from enum import Enum

NUMBER_OF_PRISONERS = 100
NUMBER_OF_BOXES_TO_CHECK = 50
NUMBER_OF_ITERATIONS = 1000000


class Strategy(Enum):
    NAIVE = 1
    EFFICIENT = 2


MODE = Strategy.EFFICIENT


def main() -> None:
    number_successful_iterations = 0
    print("Starting prisoner problem simulation...")
    for _ in range(NUMBER_OF_ITERATIONS):
        boxes = setup_random_boxes(NUMBER_OF_PRISONERS)
        match MODE:
            case Strategy.NAIVE:
                if naive_strategy(boxes):
                    number_successful_iterations += 1
            case Strategy.EFFICIENT:
                if efficient_strategy(boxes):
                    number_successful_iterations += 1
            case _:
                raise ValueError("Invalid strategy")

    print("Simulation finished.")
    print(f"Number of successful iterations: {number_successful_iterations}")
    print(f"Number of iterations: {NUMBER_OF_ITERATIONS}")
    print(
        f"Probability of success: {number_successful_iterations / NUMBER_OF_ITERATIONS}"
    )


def setup_random_boxes(number_of_prisoners: int) -> list[int]:
    numbers = list(range(1, number_of_prisoners + 1))
    boxes = [0] * number_of_prisoners
    for j in range(number_of_prisoners):
        boxes[j] = numbers.pop(random.randint(0, len(numbers) - 1))
    return boxes


def naive_strategy(boxes: list[int]) -> bool:
    # Naive strategy is to look at random boxes
    prisoners = setup_random_boxes(NUMBER_OF_PRISONERS)
    for prisoner in prisoners:
        boxes_to_search = boxes[:]
        found_their_box = False
        for _ in range(NUMBER_OF_BOXES_TO_CHECK):
            box_searched = boxes_to_search.pop(
                random.randint(0, len(boxes_to_search) - 1)
            )
            if box_searched == prisoner:
                found_their_box = True
                break
        if not found_their_box:
            return False
    return True


def efficient_strategy(boxes: list[int]) -> bool:
    # Efficient strategy is to look at the boxes of their number and then follow
    # the boxes
    prisoners = setup_random_boxes(NUMBER_OF_PRISONERS)
    for prisoner in prisoners:
        found_their_box = False
        box_searched = boxes[prisoner - 1]
        if box_searched == prisoner:
            found_their_box = True
        boxes_searched = 1
        while boxes_searched <= NUMBER_OF_BOXES_TO_CHECK and not found_their_box:
            box_searched = boxes[box_searched - 1]
            if box_searched == prisoner:
                found_their_box = True
            boxes_searched += 1
        if not found_their_box:
            return False
    return True


if __name__ == "__main__":
    main()
