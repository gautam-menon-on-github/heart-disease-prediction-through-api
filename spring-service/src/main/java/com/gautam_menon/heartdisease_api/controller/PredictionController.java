package com.gautam_menon.heartdisease_api.controller;

import com.gautam_menon.heartdisease_api.dto.HeartDiseaseApiRequest;
import com.gautam_menon.heartdisease_api.dto.PredictionResponse;
import com.gautam_menon.heartdisease_api.service.PredictionService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
@RequiredArgsConstructor
public class PredictionController {

    private final PredictionService predictionService;

    @PostMapping("/predictions")
    public ResponseEntity<PredictionResponse> predict(@Valid @RequestBody HeartDiseaseApiRequest request) {
        return ResponseEntity.ok(predictionService.predict(request));
    }



}
