def FIFO(pages, frame_count):
    frame = []
    page_faults = 0
    page_hits = 0
    for page in pages:
        if page in frame:
            page_hits += 1
        else:
            if len(frame) == frame_count:
                frame.pop(0)
            frame.append(page)
            page_faults += 1
    return page_faults, page_hits

def LRU(pages, frame_count):
    frame = []
    page_faults = 0
    page_hits = 0
    for page in pages:
        if page in frame:
            page_hits += 1
            frame.pop(frame.index(page))
            frame.append(page)
        else:
            if len(frame) == frame_count:
                frame.pop(frame.index(min(frame, key=lambda x: frame.index(x))))
            frame.append(page)
            page_faults += 1
    return page_faults, page_hits

def Optimal(pages, frame_count):
    frame = []
    page_faults = 0
    page_hits = 0
    for index, page in enumerate(pages):
        if page in frame:
            page_hits += 1
        else:
            if len(frame) == frame_count:
                future_pages = pages[index+1:]
                replace = min(frame, key=lambda x: future_pages.index(x) if x in future_pages else float('inf'))
                frame.pop(frame.index(replace))
            frame.append(page)
            page_faults += 1
    return page_faults, page_hits

if __name__ == "__main__":
    algorithms = {"FIFO": FIFO, "LRU": LRU, "Optimal": Optimal}
    algorithm = input("Enter the algorithm (FIFO, LRU, Optimal): ").strip()
    if algorithm not in algorithms:
        print("Invalid algorithm.")
        exit()

    frame_count = int(input("Enter the number of page frames: "))
    pages = list(map(int, input("Enter the page sequence separated by spaces: ").strip().split()))

    page_faults, page_hits = algorithms[algorithm](pages, frame_count)

    print(f"Number of page faults ({algorithm}): {page_faults}")
    print(f"Number of page hits ({algorithm}): {page_hits}")
    print(f"Ratio of page faults to page hits ({algorithm}): {page_faults / (page_faults + page_hits)}")
    print()
