package com.gautam_menon.heartdisease_api.config;

import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.JdkClientHttpRequestFactory;
import org.springframework.web.client.RestClient;

import java.net.http.HttpClient;

@Configuration
@EnableConfigurationProperties(ModelServiceProperties.class)
public class RestClientConfig {

    @Bean
    public RestClient modelServiceRestClient(ModelServiceProperties properties) {
        HttpClient httpClient = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_1_1)
                .build();

        return RestClient.builder()
                .baseUrl(properties.baseUrl())
                .requestFactory(new JdkClientHttpRequestFactory(httpClient))
                .build();
    }
}