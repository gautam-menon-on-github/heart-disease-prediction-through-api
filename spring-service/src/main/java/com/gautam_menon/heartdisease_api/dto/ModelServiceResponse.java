package com.gautam_menon.heartdisease_api.dto;

import lombok.Data;

@Data
public class ModelServiceResponse {
    private Integer prediction;
    private Float probability;
    private String modelVersion;
}
