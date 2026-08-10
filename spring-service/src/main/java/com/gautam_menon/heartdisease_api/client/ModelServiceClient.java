package com.gautam_menon.heartdisease_api.client;

import com.gautam_menon.heartdisease_api.dto.HeartDiseaseApiRequest;
import com.gautam_menon.heartdisease_api.dto.ModelServiceResponse;
import com.gautam_menon.heartdisease_api.exception.ModelServiceException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;

import java.util.HashMap;
import java.util.Map;

@Component
@RequiredArgsConstructor
@Slf4j
public class ModelServiceClient {

    private final RestClient modelServiceRestClient;

    public ModelServiceResponse getPrediction(HeartDiseaseApiRequest request) {
        Map<String, Object> payload = toModelPayload(request);
        log.info("Sending payload to model service: {}", payload);

        try {
            return modelServiceRestClient.post()
                    .uri("/predict")
                    .contentType(MediaType.APPLICATION_JSON)
                    .body(payload)
                    .retrieve()
                    .body(ModelServiceResponse.class);
        } catch (Exception e) {
            log.error("Model service call failed", e);
            throw new ModelServiceException("Failed to get prediction from model service", e);
        }
    }

    private Map<String, Object> toModelPayload(HeartDiseaseApiRequest r) {
        Map<String, Object> payload = new HashMap<>();
        payload.put("age", r.getAge());
        payload.put("sex", r.getSex());
        payload.put("chest_pain_type", r.getChestPainType());
        payload.put("resting_bp", r.getRestingBp());
        payload.put("cholesterol", r.getCholesterol());
        payload.put("fasting_bs", r.getFastingBs());
        payload.put("resting_ecg", r.getRestingEcg());
        payload.put("max_hr", r.getMaxHr());
        payload.put("exercise_angina", r.getExerciseAngina());
        payload.put("oldpeak", r.getOldpeak());
        payload.put("st_slope", r.getStSlope());
        return payload;
    }
}
