# Gets the median of a list
def get_median(m_list: list) -> int | float:
    # List is empty, return 0
    if m_list == []:
        return 0

    if len(m_list) % 2 == 0:
        return (int(m_list[len(m_list)//2-1])+int(m_list[len(m_list)//2]))/2

    return m_list[len(m_list)//2]
