# The Shadow Campaigns: Dissecting the 2025 Financial Battleground of Washington State Politics

### PREFACE: Reproducing This Dataset
Due to GitHub’s file size limits for data repositories, the raw dataset used for this analysis is not directly uploaded to this repository. However, you can perfectly recreate my dataset by downloading it directly from the Washington State Public Disclosure Commission (PDC) Open Data Portal. 

**Data Source:** [Washington State PDC - Contributions to Candidates and Political Committees]((https://data.wa.gov/Politics/Contributions-to-Candidates-and-Political-Committe/kv7h-kjye/about_data))

**Filters Applied for Download:**
To isolate the most relevant data for the 2025 election cycle and eliminate statistical noise, the following filters were applied before exporting:
1. **Date Range:** Filtered for receipt dates between `2024` and `2026` to capture early and late reporting for the `2025` election year.
2. **Amount:** Filtered for contributions `>= $10.00`. (Contributions under ten dollars were excluded because they overwhelmingly consisted of bank interest accruals, testing transactions, and other irrelevant data points).

---

### The Curiosity: Is Politics Still Local?
When we read the news or watch campaign advertisements, the media heavily emphasizes the grassroots nature of state-level politics. Candidates are constantly touting their "small-dollar donations" and framing their campaigns as neighbor-to-neighbor movements. As a data enthusiast, I was deeply curious: does the math actually support this narrative in Washington State? 

If we look at the raw financial receipts of the 2025 election cycle, who is truly bankrolling the elections? Is it the local barista and teacher, or is it a network of mega-donors and out-of-state tech executives? More importantly, when we look at the entities receiving these millions of dollars, are they actually the politicians whose names appear on the ballot, or are they shadow organizations? 

### The Investigation: Separating Individuals from Groups
To find the truth, I downloaded the state’s political contribution receipts and loaded them into Malloy. My investigation required a structural dismantling of how the data is traditionally viewed. 

Typically, state dashboards lump all contributions together to show a single "Total Raised" number. Instead, I built a custom Malloy model to strictly separate the data. First, I split the "Filers" (the entities receiving the money) into two groups: actual human **Candidates** and non-human **Political Action Committees (PACs)**. Then, I split the "Donors" into **Individual Humans** and **Organizations/Corporations**. Finally, I cleaned up the demographic data, removing null values and standardizing inputs so I could accurately map out the occupations and geographic origins of the donors.

![Filer Comparison Bar Chart](img/candidates_vs_pacs.png)
*(Screenshot: A comparison of the top Candidates vs. the top PACs receiving funds)*

### The Surprises: The Death of the "Candidate"
As I ran my Malloy queries, the traditional "Candidate vs. Candidate" narrative completely fell apart, revealing several massive surprises.

**Surprise 1: PACs Completely Crush Individual Politicians**
I expected a high-profile, state-level politician to be the top earner. However, the top candidate filer in the state—Girmay Zahilay—raised an impressive $1.33 million, which pales in comparison to the PACs. The *SEIU 775 Ballot Fund* pulled in a staggering **$9.6 million**, and Airbnb's *HOST PAC* brought in nearly **$4 million**. The top 5 PACs alone raised over $22 million, vastly out-earning the actual human beings running for office. The real financial battles aren't happening between candidates; they are happening in the shadows via Ballot Initiatives.

![Mega Donors Chart](img/human_vs_org_donors.png)
*(Screenshot: Top Individual Mega-Donors vs Organizational Donors)*

**Surprise 2: The Mega-Donor Reality**
Looking at the donors, I expected to see a massive volume of everyday citizens. While "Small Contributions" do mathematically add up, I was shocked to find that specific, ultra-wealthy individuals operate on the same financial tier as major corporations. For example, Brian Heywood personally contributed over **$1.6 million**, and Steve Gordon contributed over $726,000. 

**Surprise 3: "Retired" is the Ultimate Occupation**
By cleaning the occupation data, a massive demographic truth emerged. I assumed tech workers or lawyers would be the top donors. Instead, **"RETIRED"** individuals contributed over **$7.1 million** to political campaigns. The next closest active occupation was "CEO" at $2.3 million. The non-working class is outspending the working class by a ratio of 3-to-1.

![Occupations Chart](img/top_occupations.png)
*(Screenshot: The overwhelming financial dominance of Retired donors)*

**Surprise 4: Out-of-State Influence**
Finally, looking at the geography of these donations, I was surprised to see that Washington’s local elections are viewed as a national battleground. Over **$25 million** of the total funds came from donors residing entirely outside of Washington state, heavily clustered in California and Washington D.C.

### So What? (Conclusion & Impact)
This analysis proves that if we view elections strictly as "Candidate A vs. Candidate B," we are missing where the real money is moving. The data shows that the modern financial engines of state politics are massive Union and Corporate PACs backing specific ballot initiatives, heavily subsidized by retired wealth and out-of-state interests.

**Who would care about these findings?**
* **Everyday Voters:** Voters need to understand that when they see a barrage of ads for local ballot initiatives, they are often funded by multi-million dollar out-of-state war chests facing almost zero funded opposition. 
* **Campaign Managers & Strategists:** Professionals in the political sphere can use this to understand that traditional candidate fundraising is heavily outgunned. To win policy battles, tapping into PAC networks and the "Retired" demographic is statistically much more effective than grassroots outreach.
* **Journalists & Watchdogs:** Media organizations can use these specific models to shift their reporting away from partisan horse races and focus on the shadow PACs that actually control the vast majority of the state's political capital.
