package com.gautam_menon.heartdisease_api.dto;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class PredictionResponse {
    private Integer prediction;
    private Float probability;
    private String riskLevel; // this will be LOW/MODERATE/HIGH derived from probability.
}
