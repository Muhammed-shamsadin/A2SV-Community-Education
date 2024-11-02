class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_citation = max(citations)
        counts = [0] * (max_citation + 1)
        
        # Step 1: Count the number of papers for each citation count
        for citation in citations:
            counts[citation] += 1
        
        total_papers = 0
        
        # Step 2: Calculate how many papers have at least `h` citations
        for h in range(max_citation, -1, -1):
            total_papers += counts[h]
            if total_papers >= h:
                return h
        
        return 0  # Fallback