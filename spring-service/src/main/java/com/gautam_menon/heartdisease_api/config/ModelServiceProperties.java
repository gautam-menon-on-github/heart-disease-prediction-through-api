package com.gautam_menon.heartdisease_api.config;

import org.springframework.boot.context.properties.ConfigurationProperties;

@ConfigurationProperties(prefix = "model-service")
public record ModelServiceProperties(String baseUrl) {}