package com.gautam_menon.heartdisease_api.service;

import com.gautam_menon.heartdisease_api.client.ModelServiceClient;
import com.gautam_menon.heartdisease_api.dto.HeartDiseaseApiRequest;
import com.gautam_menon.heartdisease_api.dto.ModelServiceResponse;
import com.gautam_menon.heartdisease_api.dto.PredictionResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PredictionService {

    private final ModelServiceClient modelServiceClient;

    public PredictionResponse predict(HeartDiseaseApiRequest request) {
        ModelServiceResponse modelResponse = modelServiceClient.getPrediction(request);
        String riskLevel = deriveRiskLevel(modelResponse.getProbability());

        return new PredictionResponse(
                modelResponse.getPrediction(),
                modelResponse.getProbability(),
                riskLevel
        );

    }

    private String deriveRiskLevel(Float probability) {
        if (probability < 0.3) return "LOW";
        else if (probability < 0.7) return "MEDIUM";
        else return "HIGH";
    }

}
