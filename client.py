# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Community Ambassador Client
Pure Python Standard Library (Zero External Dependencies)
Implements sentiment momentum vector analysis, contributor reputation Eigenvector centrality,
and toxic discourse damping factor modeling.
"""

import math
from typing import Dict, Any, List, Optional

class OpenClawGenParkCommunityAmbassador:
    """
    Decentralized developer relations and community governance dynamics engine.
    """

    def __init__(self):
        pass

    def calculate_sentiment_momentum_vector(
        self,
        sentiment_series: List[float],
        decay_alpha: float = 0.3
    ) -> Dict[str, Any]:
        """
        Calculates Exponential Moving Average (EMA) and velocity momentum of community sentiment:
          EMA_t = alpha * S_t + (1 - alpha) * EMA_{t-1}
          Momentum = EMA_t - EMA_{t-1}
        """
        if not sentiment_series:
            return {"current_ema": 0.0, "momentum": 0.0, "sentiment_trajectory": "FLAT"}

        ema = sentiment_series[0]
        ema_history = [round(ema, 4)]
        momentum = 0.0

        for s in sentiment_series[1:]:
            prev_ema = ema
            ema = decay_alpha * s + (1.0 - decay_alpha) * prev_ema
            momentum = ema - prev_ema
            ema_history.append(round(ema, 4))

        momentum = round(momentum, 4)
        current_ema = round(ema, 4)

        if momentum >= 0.05:
            traj = "SURGING_POSITIVE_ADOPTION"
        elif momentum <= -0.05:
            traj = "DECLINING_SENTIMENT_DRIFT"
        else:
            traj = "STABLE_EQUILIBRIUM"

        return {
            "current_ema_sentiment": current_ema,
            "sentiment_momentum_gradient": momentum,
            "sentiment_trajectory": traj,
            "ema_history": ema_history
        }

    def compute_contributor_eigenvector_centrality(
        self,
        node_ids: List[str],
        interaction_matrix: List[List[float]],
        max_iterations: int = 50,
        convergence_tolerance: float = 1e-5
    ) -> Dict[str, Any]:
        """
        Computes contributor prestige / influence using Power Iteration Eigenvector Centrality:
          x_{k+1} = A * x_k / || A * x_k ||
        Identifies key community anchors and core maintainers.
        """
        n = len(node_ids)
        if n == 0 or len(interaction_matrix) != n:
            return {"centrality_scores": {}, "convergence_iterations": 0}

        # Initial uniform vector
        v = [1.0 / math.sqrt(n)] * n

        for it in range(max_iterations):
            # Matrix-vector multiplication A * v
            next_v = [0.0] * n
            for i in range(n):
                for j in range(n):
                    next_v[i] += interaction_matrix[i][j] * v[j]

            # Vector norm
            norm = math.sqrt(sum(x**2 for x in next_v))
            if norm == 0.0:
                break
            next_v = [x / norm for x in next_v]

            # Check convergence
            diff = math.sqrt(sum((next_v[i] - v[i]) ** 2 for i in range(n)))
            v = next_v
            if diff < convergence_tolerance:
                break

        # Map scores to nodes
        scores = {node_ids[i]: round(v[i], 4) for i in range(n)}
        sorted_ranks = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)

        return {
            "total_nodes": n,
            "top_contributor": sorted_ranks[0][0] if sorted_ranks else None,
            "centrality_scores": scores,
            "ranked_influencers": [{"contributor": k, "centrality": val} for k, val in sorted_ranks]
        }

    def evaluate_toxic_discourse_damping(
        self,
        flagged_toxicity_incidents: int,
        total_community_messages: int,
        damping_intervention_effectiveness_pct: float = 80.0
    ) -> Dict[str, Any]:
        """
        Models community moderation damping factor:
          ToxicityRate = Flagged / Total
          PostInterventionRate = ToxicityRate * (1 - Effectiveness)
        """
        total = max(1, total_community_messages)
        raw_rate = (flagged_toxicity_incidents / total) * 100.0
        damped_rate = raw_rate * (1.0 - (damping_intervention_effectiveness_pct / 100.0))

        if damped_rate <= 0.5:
            health = "HEALTHY_COLLABORATIVE"
        elif damped_rate <= 2.0:
            health = "MODERATE_FRICTION"
        else:
            health = "TOXIC_ESCALATION_THREAT"

        return {
            "total_messages_audited": total,
            "flagged_incidents": flagged_toxicity_incidents,
            "baseline_toxicity_rate_pct": round(raw_rate, 3),
            "damped_post_intervention_rate_pct": round(damped_rate, 3),
            "community_health_status": health
        }
