# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Community Ambassador MCP Server
FastMCP standard interface for sentiment momentum and contributor centrality scoring.
"""

import json
from typing import Dict, Any, List
from client import OpenClawGenParkCommunityAmbassador

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('openclaw-genpark-community-ambassador')

ambassador = OpenClawGenParkCommunityAmbassador()

@mcp.tool()
def calculate_sentiment_momentum_vector(
    sentiment_series: List[float],
    decay_alpha: float = 0.3
) -> str:
    """
    Calculates Exponential Moving Average and velocity momentum of community sentiment.
    """
    res = ambassador.calculate_sentiment_momentum_vector(sentiment_series, decay_alpha)
    return json.dumps(res, indent=2)

@mcp.tool()
def compute_contributor_eigenvector_centrality(
    node_ids: List[str],
    interaction_matrix: List[List[float]]
) -> str:
    """
    Computes contributor prestige / influence using Power Iteration Eigenvector Centrality.
    """
    res = ambassador.compute_contributor_eigenvector_centrality(node_ids, interaction_matrix)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_toxic_discourse_damping(
    flagged_toxicity_incidents: int,
    total_community_messages: int,
    damping_intervention_effectiveness_pct: float = 80.0
) -> str:
    """
    Models community moderation damping factor and post-intervention toxicity.
    """
    res = ambassador.evaluate_toxic_discourse_damping(flagged_toxicity_incidents, total_community_messages, damping_intervention_effectiveness_pct)
    return json.dumps(res, indent=2)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
