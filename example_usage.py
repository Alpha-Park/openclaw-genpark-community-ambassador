# -*- coding: utf-8 -*-
from client import OpenClawGenParkCommunityAmbassador

amb = OpenClawGenParkCommunityAmbassador()

# 1. Sentiment Momentum Vector
sentiments = [0.15, 0.25, 0.35, 0.55, 0.70]
mom = amb.calculate_sentiment_momentum_vector(sentiments, decay_alpha=0.35)
print(f"Sentiment Momentum: EMA={mom['current_ema_sentiment']} (Gradient={mom['sentiment_momentum_gradient']}, {mom['sentiment_trajectory']})")

# 2. Contributor Centrality
nodes = ["alice_core", "bob_dev", "charlie_mod", "david_koc"]
interactions = [
    [0.0, 5.0, 2.0, 1.0],
    [5.0, 0.0, 1.0, 0.0],
    [2.0, 1.0, 0.0, 4.0],
    [1.0, 0.0, 4.0, 0.0]
]
centrality = amb.compute_contributor_eigenvector_centrality(nodes, interactions)
print()
print(f"Eigenvector Centrality: Top Contributor={centrality['top_contributor']}")
for inf in centrality['ranked_influencers']:
    print(f"  {inf['contributor']}: {inf['centrality']}")

# 3. Toxic Discourse Damping
toxic = amb.evaluate_toxic_discourse_damping(flagged_toxicity_incidents=12, total_community_messages=1500)
print()
print(f"Community Moderation Damping: Damped Rate={toxic['damped_post_intervention_rate_pct']}% ({toxic['community_health_status']})")
